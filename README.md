# CD-Example

The goal is to create a simple development-to-production pipeline thru Github, a CI/CD (Contiueous Integration and Continuous Delivery) automation.
When the code of this application is pushed from the local development server to Github, actions will be triggered to test the code and on no failure files will be copied to the production server on DigitalOcean and when that has succeeded all the modules used will be upgraded to match the development ones and restart the app.

To achieve this, I did the following:
1. Creating SSH keys to access DigitalOcean (production server) from the local development server and also from Github and disable password authentication on production.
2. Preparing the production server by creating a `cd-example` directory and installing and configurate NGINX, Python, Flask and Gunicorn.
3. Created a Github Action with three Jobs all executed after each other.
    - First Job tests the code with Pytest
    - Second Job starts when first job has been passed successfully. This will only copy files needed for production and athe `update.sh` script and the `requirements.txt` file.
    - Third Job upgrades the modules and restarts the app on production.

## Problem solving
The first problem to solve was to get a good grasp of which key is stored where ad how it is recognized by the other server. My SSH agent on my local server didn't recognize my private key when starting a new connection and I had to added again, before creating a new SSH connection.

Another problem was avoiding a Git conflict when pushing a repo to production and production was altered for some reason. But why would the final release on production having commits. Also all the files not neccessary for a production environment will also be copied. So I choose to copy only the necessary files for production (plus some files to update modules after copy).

Only copying files to production is not an option when modules are updated on development. So i made a script updating modules on the production side.

## Conclusion
With this assignment I learnt a lot about Github Actions and DevOps. It's a frustration when things are not working as intended but a joy when one ultimately sees the green light :-) 



