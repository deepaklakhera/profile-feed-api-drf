# profile-feed-api-drf
Api's created using django rest framework.This includes creating custom user and creating a profile-feed-api


Custom UserModel allows user to signin using Email field.
Aftercreating a customusermodel we have to Update customUsermodelmanager for our model and we can use it anywhere in the the project by updating AUTH_USER_MODEL in Settings.py

We have used Viewsets and ApiView for creating rest api's.

The api's show simple functionalities of a profile-feed.

Also, we have used rest_framework Token authentication
