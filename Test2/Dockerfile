FROM python

#Sets up working directory 
WORKDIR /app

#Copy the requirements.txt file to the container
#COPY requirements.txt . 
#But I can copy all files

COPY . . 

#Intalling the requred librares
RUN pip install --no-cache-dir -r requirements.txt

#sets the environment var for display (That's needed, because of the GUI)
ENV DISPLAY=:0

#Runs the python app
CMD [ "python", "main.py"]