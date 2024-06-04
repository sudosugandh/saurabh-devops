# Use the official Python image as the base image
FROM python:3.9-slim as builder

# Set the working directory for the new stage
WORKDIR /app

# Copy the source code and dependencies from the builder stage
COPY --from=builder /app .

# Expose any necessary ports
EXPOSE 3000

# Command to run the application
CMD ["python", "parse_xml.py"]
