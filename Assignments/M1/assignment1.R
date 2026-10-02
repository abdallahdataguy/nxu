# Import of base functions is not required here as I did in Python.

# Step 1: Generate a random list of 400 workers with their attributes
workers_list <- list()
for (i in seq_len(400)) {
    worker <- list(
        id = i,
        name = sprintf("Worker%03d", i),
        age = sample(18:65, 1),
        sex = sample(c("male", "female"), 1),
        department = sprintf("Department %d", sample(1:10, 1)),
        salary = sample(1000:100000, 1)
    )
    workers_list[[i]] <- worker
}

# Step 2: For each worker, conditionally generate a payment slip
# handle any potential errors that may arise
for (i in seq_along(workers_list)) {
    worker <- workers_list[[i]]
    salary <- worker[["salary"]]
    worker <- tryCatch({
        if (salary > 7500 && salary < 30000 && worker[["sex"]] == "female") {
            worker[["level"]] <- "A5-F"
        } else if (salary > 10000 && salary < 20000) {
            worker[["level"]] <- "A1"
        } else { # Other level not specified above
            worker[["level"]] <- "Other level"
        }
        worker
    }, error = function(e) {
        cat(sprintf("Error occurred while processing %s data: %s\n",
                    worker[["name"]], conditionMessage(e)))
        worker
    })
    workers_list[[i]] <- worker
}

cat("Payment slips generated successfully for all workers.\n")
