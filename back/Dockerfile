FROM python:3.7

# Install requirements
RUN pip install --no-cache-dir --upgrade pip
COPY back/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Add source code
ADD back/app /home/app
# ADD migrations /home/migrations
ADD back/requirements.txt /home
ADD back/manage.py /home

WORKDIR /home
# Set environment variables
ENV FLASK_APP=manage.py

# ENTRYPOINT
# ENTRYPOINT python manage.py run

EXPOSE 5000
#not sure if app:app works$ -> (MODULE_NAME):$(VARIABLE_NAME)
CMD ["gunicorn", "-b", "0.0.0.0:5000" ,"manage:app"]
