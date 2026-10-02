set.seed(123)

# Dynamically create a list of 400 workers 
workers <- list()
for (i in 1:400) {
  worker <- list(
    id = i,
    name = paste("Worker", i, sep = "_"),
    salary = sample(1000:50000, 1),
    sex = sample(c("Male", "Female"), 1)
  )
  workers[[i]] <- worker
}

# Generate payment slips for each worker
for (worker in workers) {
  tryCatch({
    salary <- worker$salary
    sex <- worker$sex
    
    # Apply the conditional statements
    if (salary > 7500 & salary < 30000 & sex == "Female") {
      worker$level <- 'A5-F'
    } else if (salary > 10000 & salary < 20000) {
      worker$level <- 'A1'
    } else {
      worker$level <- 'Other' # Default level if no conditions are met
    }
    
    # Print payment slips
    cat("Payment Slip: ID=", worker$id, ", Name=", worker$name, 
        ", Salary=", worker$salary, ", Sex=", worker$sex,
        ", Level=", worker$level, "\n", sep = "")
  }, 
  
  # Exception handling for potential errors
  error = function(e) {
    cat("Error processing worker", worker$id, ":", conditionMessage(e), "\n")
  })
}
