#Educational Authentication Bypass Demonstration

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Framework-Flask-black?style=for-the-badge&logo=flask)
![Security](https://img.shields.io/badge/Security-Educational-green?style=for-the-badge)

An academic demonstration of an HTTP POST brute-force vulnerability. This project features a full "Attacker-Victim" architecture hosted entirely on a local machine to safely demonstrate how automated authentication bypass attacks operate across a network, and how developers can defend against them.

## 🏗️ System Architecture

This project consists of two isolated Python scripts communicating over a local network (`127.0.0.1`):

1. **The Victim Server (`server.py`):** A lightweight web application built with Flask. It hosts a functional HTML login portal on Port 5000 that processes `POST` requests and evaluates credentials against a hardcoded backend validation system.
   
2. **The Attacker Script (`bruteforce.py`):** An automated automation tool utilizing the Python `requests` library. It systematically reads payloads from a wordlist, packages them into HTTP form data, and rapidly fires them at the target endpoint while parsing the server's HTML responses to detect a successful bypass.

## Prerequisites

To run this demonstration locally, you will need Python installed along with the `Flask` and `requests` libraries.

```bash
# Install required dependencies
pip install Flask requests
