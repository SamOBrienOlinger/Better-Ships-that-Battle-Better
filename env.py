# env.py - Local Development Environment Variables

# DEBUG/DEV: Set to True for local development
# These will be overridden by Heroku's False values in production.
DEBUG = True
DEV = True

# SECURITY: Must match the value set on Heroku
SECRET_KEY = 'piratequeensseabattles2025'

# DATABASE: The new, correct, dedicated URL
DATABASE_URL = 'postgres://u4o4iphdt49fhi:p8d8f824787ab0bddad5e113e19bb564227cebcea7224ceaebb01213d9601cf02@c2hbg00ac72j9d.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d2me2a6u8iis7t'

# CLOUDINARY: USE YOUR FULL CLOUDINARY URL HERE
CLOUDYNARY_URL = 'PASTE_YOUR_FULL_CLOUDINARY_URL_HERE'

# OTHER VARIABLES: Use the final, correct host
ALLOWED_HOST = 'pirate-queens-sea-battles-a92eba2c9a74.herokuapp.com'
DISABLE_COLLECTSTATIC = '1'
