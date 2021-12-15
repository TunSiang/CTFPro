# Backend

Backend for frontend

Tested on a fresh install of ubuntu 20.04.3 Desktop

## Steps:

Python 3.7 or greater.

Setup getting the CTFPro with git.

```bash
sudo apt install git
cd Desktop
git clone https://github.com/TunSiang/CTFPro.git
```

Setup [install_req.sh] file.

```bash
sudo chmod 777 /home/{your_username}/Desktop/CTFPro/api/scripts/install_req.sh
yes | ./home/{your_username}/Desktop/CTFPro/api/scripts/install_req.sh
```

Setup [awscli](https://github.com/aws/aws-cli/tree/v2).

```bash
aws configure
```

Setup [local_mysql_db].

```bash
sudo mysql

CREATE USER 'sammy'@'localhost' IDENTIFIED BY 'password';

GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'sammy'@'localhost' WITH GRANT OPTION;

FLUSH PRIVILEGES;

exit


# Now log in as sammy 

mysql -u sammy -p   # Password is password

CREATE DATABASE ncl;

use ncl;

create table users (
username varchar(45) NOT NULL PRIMARY KEY, 
password varchar(45) NOT NULL,
email varchar(45) NOT NULL, 
institution varchar(45) NOT NULL
);

INSERT INTO users VALUE ("billy", "password", "billy@ncl.com", "NCL");

INSERT INTO users VALUE ("axe", "password", "axe@ncl.com", "NCL");

create table component (
component_id int AUTO_INCREMENT PRIMARY KEY, 
type varchar(45) NOT NULL, 
hostname varchar(45) NOT NULL,
state varchar(45) NOT NULL,
URL_access varchar(45) NOT NULL, 
username varchar(45) NOT NULL,
CONSTRAINT fk_name
FOREIGN KEY (username) 
        REFERENCES users(username)
);

exit

```


### Usage

```bash
cd /home/{your_username}/Desktop/CTFPro/api
uvicorn main:app --host 0.0.0.0 --port 8000

# Access/ find out your ip address with ifconfig
ifconfig

# Test out the different api calls using the Swagger UL at " http://{your_ip}:8000/docs".

# Example list all
![image](https://user-images.githubusercontent.com/78256625/146099280-f1647868-a8a9-47e2-82d6-7dae23666d1e.png)
(Since we only created user billy in our db we can only use billy)

# Example list selected
![image](https://user-images.githubusercontent.com/78256625/146099507-a84a8b9f-f919-4201-adb0-b5a1a228cbe1.png)
(User billy and the selected instance name to query)

# Example Create instance
![image](https://user-images.githubusercontent.com/78256625/146099665-6ba8a3d5-8073-49aa-90e7-44efd730a583.png)
(In this example, we are provisioning 2 instances one virtualbox named "fish", another instance is aws named "cow".
If {component_name}=true means that you want to provison this instance, default all is set to true, please check to make sure which component to provison or else it willhave an error.)

(Note! that right now there is no installing the ctfd script or etc just for testing aka making it faster to provision/test.)

# Example stopping/starting an instance
![image](https://user-images.githubusercontent.com/78256625/146100278-8ec1c67e-7e02-4e69-b025-2cc8cf038968.png)
![image](https://user-images.githubusercontent.com/78256625/146100405-98516643-4617-416b-8133-463e0df52339.png)
(In the first picture is stopping the instance, make sure that under {cur_state} is stop, if you want to start it change it to start.)
(Right now it will only check for start and stop, will need to create an exception to catch any other values.)

# Example Deleting a instance
![image](https://user-images.githubusercontent.com/78256625/146100581-018834c5-5336-4f60-b4d0-d1e28ba3adcb.png)
(Deleting the instance using instance name.)

ALL this is with CRUD, storing the info into the db and using the db to get the info out.


```

### Errors
Make sure that your AMI is correct (checking the region and the AMI).
I got this error where AMI is not recognised even though it is the correct AMI, later i know that the AMI was updated recently for my region.
Even after updating the AMI and restarting the uvicorn, it still gives the error, only after deleting that Vagrantfile and creating a new one with the same settings does it work again. 
