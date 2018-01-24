# observeit
 
when i commit and push the GIT data where html and pyton script is


in the git server: (for example our puppet linux)

script   /git/puppet.git/hooks/post-receive

     #it will call script: web-post-receive.sh


web-post-receive.sh : will kill process, then copy new data (html)  and start flask service






if its windows


net stop WAS

xcopy *.* C:\inetpub\wwwroot\ /y /r /c

net start WAS

#or:  

Start /w pkgmgr /iu:IIS-WebServerRole;IIS-WebServer;IIS-CommonHttpFeatures;IIS-StaticContent;IIS-DefaultDocument;IIS-DirectoryBrowsing;IIS-HttpErrors;IIS-HealthAndDiagnostics;IIS-HttpLogging;IIS-LoggingLibraries;IIS-RequestMonitor;IIS-Security;IIS-RequestFiltering;IIS-HttpCompressionStatic;IIS-WebServerManagementTools;IIS-ManagementConsole;WAS-WindowsActivationService;WAS-ProcessModel;WAS-NetFxEnvironment;WAS-ConfigurationAPI

