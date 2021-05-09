#base image
FROM python
COPY . /cloud_computing
WORKDIR /cloud_computing
CMD python assignment.py
