# Python Azure function with connection pooling for Azure MySQL

The sample provides code sample on how to use connection pooling with Python Azure function. 
 

## Getting Started

### Prerequisites

- Create MySQL database in Azure (This sample uses flexible server)
- Add your client IP address in the networking section (if you are testing it from VS Code.)
- Download SSL Certificate and replace with DigiCertGlobalRootCA.crt.pem VS code and local testing.  
- Allow public access from any Azure service within Azure to this server (in networking section of MySQL) 
- Setup VS code with python.  


### Quickstart

1. git clone https://github.com/Azure-Samples/function-mysql-connection-pool-python
2. cd function-mysql-connection-pool-python
3. Change the Azure MySQL server connection details in the __iniy__.py
4. Run the sample.  



## Resources

- Using KeyVault with Azure Functions to store secrets. https://github.com/Azure-Samples/serverless-keyvault-secret-rotation-handling
- VS Code with python https://code.visualstudio.com/docs/languages/python
