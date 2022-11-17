FROM python:3.7

# Install requirements
RUN pip install --no-cache-dir --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Add source code
ADD app /home/app
# ADD migrations /home/migrations
ADD requirements.txt /home
ADD manage.py /home

WORKDIR /home
# Set environment variables
ENV FLASK_APP=manage.py

# ENTRYPOINT
# ENTRYPOINT python manage.py run

EXPOSE 5000
#not sure if app:app works$ -> (MODULE_NAME):$(VARIABLE_NAME)
CMD ["gunicorn", "-b", "0.0.0.0:5000" ,"manage:app"]
