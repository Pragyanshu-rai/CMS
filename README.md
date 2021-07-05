# **CMS** 

## Clinic Management System

CMS is an online clinic record system that can be used to book appointments and manage patient records, especially for small clinics. Patient history is stored in the database and can be accessed by the user in their dashboard.

A Clinic management web application built using Django framework for servers-side, Sqlite for database, HTML, CSS, and Javascript for client-side development. For the styling of the application, Bootstrap4 is used, and javascript and jquery is
used for the responsiveness.

Developed an OTP veriﬁcation method using a mail module to send an OTP to the registered email id and Twilio module to send an OTP to the registered mobile number.

## Features

* For Patient
        
      * View or update profile information.
      * Add or update profile picture.
      * Access many features from patient dashboard such as:
            
        - View past consultations and download the prescription.
        - Book or cancel appointments anytime.
        - keep track of your active appointments.
        - View your past appointment details.
        - View and download lab reports.

* #### For Clinic

      * Manage patient records easily.
      * Reduces overhead on the staff.
      * Manage everything using the admin panel of CMS.


##### CMS website can be accessed using the link below.
> [CMS](https://cms-wa.herokuapp.com/admin/)

##### CMS website can be accessed using the link below.
> [CMS Admin](https://cms-wa.herokuapp.com/admin/)

#### API endpoint list

> [CMS API](https://cms-wa.herokuapp.com/cms-api/)

You can use the CMS API to communicate with the server, but to do so, you must first acquire an auth token by logging in.

>*Note:- For login and registration the auth token is not required.*

##### login
In order to communicate with the server, you will need an auth token which will be generated if it does not exist by sending the username and password in JSON format.

```json
{
    "username":"example_username",
    "password":"example_password"
}   
```

>*Note:- ALL the fields are required! but the order need not be the same.*

By sending a JSON file of the same structure to this endpoint (https://cms-wa.herokuapp.com/cms-api/login/) will fetch you your auth token like this.

```json
{
    "token": "<your_auth_token>"
}
```
An auth token is only generated once.

##### register
For you to login and obtain an auth token you must first be registered to the site. In order to do so write a jsonfile of the same structure.

```json
{
    "user": {
        "username": "example_username",
        "password": "example_password",
        "first_name": "example_firstname",
        "last_name": "example_lastname",
        "email": "example_email" // must be a valid email
    },
    "gender": "gender", //gender can be Male, Female or Other
    "dob": "date", //format YYYY-MM-DD
    "address": "example_address",
    "phone": "xxxxxxxxxx" //10 digit valid number
}
```

>*Note:- ALL the fields are required except last_name can be "".*

By Sending the above request you will get the following response if there is no error in the json file. 

```json



```

> *Note:- The auth token assigned to you must be included in the header of the JSON file.          
>  The header must in key: value format i.e*                                 
     **"Authorization":"token <your_auth_token>"**




