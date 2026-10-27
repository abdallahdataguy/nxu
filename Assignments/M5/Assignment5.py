# Milestone Assignment 2: Principal Component Analysis

# Import libraries and start Spark
from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType
from pyspark.sql.functions import col, isnan, when, sum as spark_sum
from pyspark.ml import Pipeline
from pyspark.ml.feature import Imputer, VectorAssembler, StandardScaler, PCA
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

folder = Path(__file__).resolve().parent
spark = (SparkSession.builder.master('local[2]').appName('BreastCancerPCA')
         .config('spark.sql.shuffle.partitions', '2').getOrCreate())
spark.sparkContext.setLogLevel('ERROR')

try:
    # Define the schema and load the referral file
    features = [
        'mean_radius', 'mean_texture', 'mean_perimeter', 'mean_area',
        'mean_smoothness', 'mean_compactness', 'mean_concavity',
        'mean_concave_points', 'mean_symmetry', 'mean_fractal_dimension',
        'radius_error', 'texture_error', 'perimeter_error', 'area_error',
        'smoothness_error', 'compactness_error', 'concavity_error',
        'concave_points_error', 'symmetry_error', 'fractal_dimension_error',
        'worst_radius', 'worst_texture', 'worst_perimeter', 'worst_area',
        'worst_smoothness', 'worst_compactness', 'worst_concavity',
        'worst_concave_points', 'worst_symmetry', 'worst_fractal_dimension'
    ]
    schema = StructType(
        [StructField('patient_id', StringType())]
        + [StructField(name, DoubleType()) for name in features]
        + [StructField('diagnosis', StringType())]
    )
    raw = spark.read.csv(str(folder / 'breast_cancer_referrals.csv'),
                         header=True, schema=schema, mode='FAILFAST')

    # Remove duplicates and count missing feature values
    data = raw.dropDuplicates().cache()
    missing = data.select([
        spark_sum(when(col(name).isNull() | isnan(col(name)), 1).otherwise(0)).alias(name)
        for name in features
    ]).first().asDict()

    # Fill missing features, assemble and standardize them
    filled = [name + '_filled' for name in features]
    imputer = Imputer(inputCols=features, outputCols=filled, strategy='median').setRelativeError(0)
    assembler = VectorAssembler(inputCols=filled, outputCol='features')
    scaler = StandardScaler(inputCol='features', outputCol='scaled',
                            withMean=True, withStd=True)

    # Reduce the standardized features to two components
    pca = PCA(k=2, inputCol='scaled', outputCol='components')
    pipeline = Pipeline(stages=[imputer, assembler, scaler, pca])
    model = pipeline.fit(data)
    result = model.transform(data)
    pca_model = model.stages[-1]
    variance = pca_model.explainedVariance.toArray()

    # Report explained variance and the largest feature weights
    lines = [
        f'Input rows: {raw.count()}',
        f'Cleaned rows: {data.count()}',
        f'Duplicates removed: {raw.count() - data.count()}',
        f'Feature columns: {len(features)}',
        'Missing values: ' + str({name: count for name, count in missing.items() if count}),
        'Missing features filled with medians; patient_id and diagnosis excluded from PCA.',
        f'PC1 explained variance: {variance[0]:.4%}',
        f'PC2 explained variance: {variance[1]:.4%}',
        f'Total explained variance: {sum(variance):.4%}'
    ]
    weights = pca_model.pc.toArray()
    for component in range(2):
        ranked = sorted(zip(features, weights[:, component]),
                        key=lambda item: abs(item[1]), reverse=True)[:5]
        lines.append(f'\nTop feature weights for PC{component + 1}:')
        lines.extend(f'{name}: {weight:.4f}' for name, weight in ranked)
    lines.append('\nFeature weights describe variation, not clinical or funding priorities.')

    # Bonus: predict diagnosis using two components and an 80/20 split
    labeled = data.filter(col('diagnosis').isin('B', 'M')).withColumn(
        'label', when(col('diagnosis') == 'M', 1.0).otherwise(0.0))
    train, test = labeled.orderBy('patient_id').randomSplit([0.8, 0.2], seed=42)
    lr = LogisticRegression(featuresCol='components', labelCol='label', maxIter=100)
    # Fit imputation, scaling, PCA, and regression on training data only.
    classifier = Pipeline(stages=[imputer, assembler, scaler, pca, lr]).fit(train)
    predictions = classifier.transform(test)
    accuracy = MulticlassClassificationEvaluator(metricName='accuracy').evaluate(predictions)
    lines.append(f'\nTraining rows: {train.count()}; test rows: {test.count()}')
    lines.append(f'Logistic regression test accuracy: {accuracy:.2%}')

    report = '\n'.join(lines)
    print(report)
    (folder / 'results.txt').write_text(report + '\n', encoding='utf-8')
    result.select('patient_id', 'diagnosis', 'components').show(5, truncate=False)
finally:
    spark.stop()
