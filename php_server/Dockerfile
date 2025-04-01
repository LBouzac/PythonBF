FROM php:8.2-apache

# Install dependencies
RUN apt-get update && \
    apt-get install -y \
    default-mysql-client \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install mysqli PHP extension for MySQL support
RUN docker-php-ext-install mysqli