# Backend

Backend for frontend

Tested on a fresh install of ubuntu 20.04.3 Desktop

## Steps:

Python 3.7 or greater.

Setup getting the CTFPro with git.

```bash
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

Setup the {your_username} to your machines username in crud.py line 118, and in the Vagrantfile line 8 and line 41

### Usage

```bash
cd /home/{your_username}/Desktop/CTFPro/api
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# Access/ find out your ip address with ifconfig
ifconfig

# Test out the different api calls using the Swagger UL at " http://{your_ip}:8000/docs".
```

### Errors
Make sure that your AMI is correct (checking the region and the AMI).
I got this error where AMI is not recognised even though it is the correct AMI, later i know that the AMI was updated recently for my region.
Even after updating the AMI and restarting the uvicorn, it still gives the error, only after deleting that Vagrantfile and creating a new one with the same settings does it work again. 
