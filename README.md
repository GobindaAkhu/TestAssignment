### Please find the both solution for "problem statement 1" and "problem statement 2" as below:

###############################################################
# Solution for problem statement 1
#################################################################

# Steps to start application on local
### Setup Local Environment for Kubernetes using minikube:

- Install minikube on my local by: brew install minikube
- Start local cluster : minikube start

### Start backend and frontend application:

- Pull the application code base on my local from (https://github.com/Vengatesh-m/qa-test)
- Check the available service list by : minikube service list
- Start the Backend service by : minikube service backend-service
- Start the Frontend service by : minikube service frontend-service

### Access the application :

- Once both backend and frontend application start we can access through browser using the url which will show on service UP example as below:
- Backend : "http://127.0.0.1:54010"
- Frontend : "http://127.0.0.1:53921"

#### Note: To see the Kubernetes dashboard we can use :  minikube dashboard



#################################################################

# Steps to run automation test

## Setup test environment:

1. Clone the repository:

   ```bash
   git clone <this_repo>
   cd this_repo
   python -m venv venv
   source venv/bin/activate
   pip install playwright
   pip install pytest-playwright
   playwright install
   pip install pytest
   
2. Run the test
   ```bash
   pytest
   
3. Verify the report:

- Open the test report "reports/html/report.html" on a browser
- There is two test case both should pass
- Test cases are written under "tests" directory


#################################################################
# Solution for problem statement 2
#################################################################


## Solution for "1. System Health Monitoring Script:"

- Solution python file : Problem_Statement_2/system_health_monitoring.py
- Sample output log for this is: Problem_Statement_2/system_health_monitoring.log

## Solution for "4. Application Health Checker:"

- Solution python file : Problem_Statement_2/application_health_checker.py
- Sample output log for this is: Problem_Statement_2/application_health_checker.log

