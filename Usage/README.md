# team1
R&amp;D Team 1 research projects

https://docs.microsoft.com/en-us/azure/app-service/containers/quickstart-python

az webapp deployment user set --user-name team1@intelex.com --password team1@intelex.com

az group create --name team1ResourceGroup --location "East US"

az appservice plan create --name team1ServicePlan --resource-group team1ResourceGroup --sku B1 --is-linux


# Bash
az webapp create --resource-group team1ResourceGroup --plan team1ServicePlan --name team1StoryPrediction --runtime "PYTHON|3.7" --deployment-local-git


--------------


bob@Azure:~$ az webapp deployment user set --user-name team1@intelex.com --password team1@intelex.com
{
  "id": null,
  "kind": null,
  "name": "web",
  "publishingPassword": null,
  "publishingPasswordHash": null,
  "publishingPasswordHashSalt": null,
  "publishingUserName": "team1@intelex.com",
  "scmUri": null,
  "type": "Microsoft.Web/publishingUsers/web"
}
bob@Azure:~$ az group create --name team1ResourceGroup --location "East US"

{
  "id": "/subscriptions/655770d5-e117-4cfc-967b-72c956c68202/resourceGroups/team1ResourceGroup",
  "location": "eastus",
  "managedBy": null,
  "name": "team1ResourceGroup",
  "properties": {
    "provisioningState": "Succeeded"
  },
  "tags": null
}
bob@Azure:~$
bob@Azure:~$ az appservice plan create --name team1ServicePlan --resource-group team1ResourceGroup --sku B1 --is-linux

{
  "adminSiteName": null,
  "freeOfferExpirationTime": "2019-01-28T20:07:38.450000",
  "geoRegion": "East US",
  "hostingEnvironmentProfile": null,
  "hyperV": false,
  "id": "/subscriptions/655770d5-e117-4cfc-967b-72c956c68202/resourceGroups/team1ResourceGroup/providers/Microsoft.Web/serverfarms/team1ServicePlan",
  "isSpot": false,
  "isXenon": false,
  "kind": "linux",
  "location": "East US",
  "maximumNumberOfWorkers": 3,
  "name": "team1ServicePlan",
  "numberOfSites": 0,
  "perSiteScaling": false,
  "provisioningState": "Succeeded",
  "reserved": true,
  "resourceGroup": "team1ResourceGroup",
  "sku": {
    "capabilities": null,
    "capacity": 1,
    "family": "B",
    "locations": null,
    "name": "B1",
    "size": "B1",
    "skuCapacity": null,
    "tier": "Basic"
  },
  "spotExpirationTime": null,
  "status": "Ready",
  "subscription": "655770d5-e117-4cfc-967b-72c956c68202",
  "tags": null,
  "targetWorkerCount": 0,
  "targetWorkerSizeId": 0,
  "type": "Microsoft.Web/serverfarms",
  "

bob@Azure:~$ az webapp create --resource-group team1ResourceGroup --plan team1ServicePlan --name team1StoryPrediction --runtime "PYTHON|3.7" --deployment-local-git

Local git is configured with url of 'https://team1@intelex.com@team1storyprediction.scm.azurewebsites.net/team1StoryPrediction.git'
{
  "availabilityState": "Normal",
  "clientAffinityEnabled": true,
  "clientCertEnabled": false,
  "cloningInfo": null,
  "containerSize": 0,
  "dailyMemoryTimeQuota": 0,
  "defaultHostName": "team1storyprediction.azurewebsites.net",
  "deploymentLocalGitUrl": "https://team1@intelex.com@team1storyprediction.scm.azurewebsites.net/team1StoryPrediction.git",
  "enabled": true,
  "enabledHostNames": [
    "team1storyprediction.azurewebsites.net",
    "team1storyprediction.scm.azurewebsites.net"
  ],
  "ftpPublishingUrl": "ftp://waws-prod-blu-077.ftp.azurewebsites.windows.net/site/wwwroot",
  "hostNameSslStates": [
    {
      "hostType": "Standard",
      "ipBasedSslResult": null,
      "ipBasedSslState": "NotConfigured",
      "name": "team1storyprediction.azurewebsites.net",
      "sslState": "Disabled",
      "thumbprint": null,
      "toUpdate": null,
      "toUpdateIpBasedSsl": null,
      "virtualIp": null
    },
    {
      "hostType": "Repository",
      "ipBasedSslResult": null,
      "ipBasedSslState": "NotConfigured",
      "name": "team1storyprediction.scm.azurewebsites.net",
      "sslState": "Disabled",
      "thumbprint": null,
      "toUpdate": null,
      "toUpdateIpBasedSsl": null,
      "virtualIp": null
    }
  ],
  "hostNames": [
    "team1storyprediction.azurewebsites.net"
  ],
  "hostNamesDisabled": false,
  "hostingEnvironmentProfile": null,
  "httpsOnly": false,
  "hyperV": false,
  "id": "/subscriptions/655770d5-e117-4cfc-967b-72c956c68202/resourceGroups/team1ResourceGroup/providers/Microsoft.Web/sites/team1StoryPrediction",
  "identity": null,
  "isDefaultContainer": null,
  "isXenon": false,
  "kind": "app,linux",
  "lastModifiedTimeUtc": "2018-12-29T20:10:03.606666",
  "location": "East US",
  "maxNumberOfWorkers": null,
  "name": "team1StoryPrediction",
  "outboundIpAddresses": "13.92.237.218,13.82.169.160,52.168.4.130,13.82.171.2,13.82.169.153",
  "possibleOutboundIpAddresses": "13.92.237.218,13.82.169.160,52.168.4.130,13.82.171.2,13.82.169.153,52.224.48.224,52.234.133.108",
  "repositorySiteName": "team1StoryPrediction",
  "reserved": true,
  "resourceGroup": "team1ResourceGroup",
  "scmSiteAlsoStopped": false,
  "serverFarmId": "/subscriptions/655770d5-e117-4cfc-967b-72c956c68202/resourceGroups/team1ResourceGroup/providers/Microsoft.Web/serverfarms/team1ServicePlan",
  "siteConfig": null,
  "slotSwapStatus": null,
  "state": "Running",
  "suspendedTill": null,
  "tags": null,
  "targetSwapSlot": null,
  "trafficManagerHostNames": null,
  "type": "Microsoft.Web/sites",
  "usageState": "Normal"
}


----------

http://team1StoryPrediction.azurewebsites.net
