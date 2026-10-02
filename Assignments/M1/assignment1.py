# Import the required libraries
from random import randint, choice

# Step 1: Generate a random list of 400 workers with their attributes
workers_list = []
for i in range(400):
    worker = {
        'id': i + 1,
        'name': f'Worker{i + 1:03d}',
        'age': randint(18, 65),
        'sex': choice(['male', 'female']),
        'department': f'Department {randint(1, 10)}',
        'salary': randint(1000, 100000)
    }
    workers_list.append(worker)

# Step 2: For each worker, conditionally generate a payment slip
# handle any potential errors that may arise
for worker in workers_list:
    salary = worker['salary']
    try:
        if salary > 7500 and salary < 30000 and worker['sex'] == 'female':
            worker['level'] = 'A5-F'
        elif salary > 10000 and salary < 20000:
            worker['level'] = 'A1'
        else: # Other level not specified above
            worker['level'] = 'Other level'
    except KeyError as e:
        print(f"Error occurred while processing {worker['name']} data: \n{e}")

print('Payment slips generated successfully for all workers.')
