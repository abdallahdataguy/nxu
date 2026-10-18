# Run this from the same folder containing notebook (.ipynb) file 
# and also make sure that you run this after running the notebook.
tryCatch({
  unzip("Employee Profile.zip", exdir = "R_Extracted")
  employee <- read.csv("R_Extracted/Employee Profile/employee_details.csv")
  print(employee, row.names = FALSE)
}, error = function(e) {
  message("Could not open profile: ", conditionMessage(e))
})
