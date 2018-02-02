import logging
 
logger = logging.getLogger("DockerWebUI")
logger.setLevel(logging.INFO)

# create the logging file handler
fh = logging.FileHandler("/var/log/dockerwebui.log")

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
# add handler to logger object
logger.addHandler(fh)
