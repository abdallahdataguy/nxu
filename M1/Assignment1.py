from random import randint, choice

# Dynamically create a list of 400 workers 
workers = []
for i in range(1, 401):
    worker = {
        'id': i,
        'name': f'Worker_{i:000}',
        'salary': randint(1000, 50000),
        'sex': choice(['Male', 'Female'])
    }
    workers.append(worker)

# Generate payment slips for each worker
for worker in workers:
    try:
        salary = worker['salary']
        gender = worker['sex']

        # Apply the conditional statements
        if 7500 < salary < 30000 and gender == 'Female':
            worker['level'] = 'A5-F'
        elif 10000 < salary < 20000:
            worker['level'] = 'A1'
        else:
            worker['level'] = 'Other'  # Default level if no conditions are met

        # Print payment slips
        print(f"Pay slip: ID={worker['id']}, Name={worker['name']}, "
              f"Salary=${worker['salary']}, Sex={worker['sex']}, Level={worker['level']}")
    
    except Exception as e:
        # Exception handling for potential errors
        print(f"Error processing worker {worker['id']}: {e}")
