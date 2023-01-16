pipeline {
agent any
environment {
 dotnet = 'C:\\Program Files\\dotnet\\dotnet.exe'
 scannerHome = tool 'DotNetSonarScanner';
}
stages {
    stage('Checkout') {
       steps {
          echo "Checkout .."
         git credentialsId: '99c56ce6-094e-42d6-be23-79c9c8e1da40', url: 'https://github.com/ravinawale/JenkinsWebApplicationDemo.git', branch: 'main'
       }
    }
    stage('Build') {
        steps {
             echo "Build .."
            bat 'dotnet build %WORKSPACE%\\JenkinsWebApplicationDemo.sln --configuration Release'
        }
    }
    stage('Publish') {
        steps {
           echo "Publish .."
           bat 'dotnet publish -c Release /p:WebPublishMethod=Package /p:ExcludeApp_Data=False /p:DesktopBuildPackageLocation="%WORKSPACE%\\JenkinsWebApplicationDemo\\bin\\Release\\net7.0\\JenkinsWebApplicationDemo.zip" /p:PackageLocation="%WORKSPACE%\\JenkinsWebApplicationDemo\\bin\\Release\\net7.0\\JenkinsWebApplicationDemo.zip" /p:PackageFileName="%WORKSPACE%\\JenkinsWebApplicationDemo\\bin\\Release\\net7.0\\JenkinsWebApplicationDemo.zip" /p:PackageAsSingleFile=true'
        }
    }
    
    stage('Test') {
        steps {
             echo "Test .."
            //bat 'dotnet test %WORKSPACE%\\TestProject1\\TestProject1.csproj'
        }
    }
    stage('Sonar') {
        steps {
            echo "Sonar .."
            //bat 'dotnet %scannerHome%\\SonarScanner.MSBuild.dll begin /k:"JenkinsWebApplicationDemo" /d:sonar.host.url="http://localhost:9000" /d:sonar.login="8d4049f031a7ff6592b6f6a43618c2f93ffb36be"'
            //bat 'dotnet build %WORKSPACE%\\JenkinsWebApplicationDemo.sln --configuration Release' 
            //bat 'dotnet %scannerHome%\\SonarScanner.MSBuild.dll end /d:sonar.login="8d4049f031a7ff6592b6f6a43618c2f93ffb36be"'
        }
    }
    stage('Deploy Stage local') {
        steps {
            echo "Deploy Stage local .."
            //Deploy application on IIS                
            //bat '"C:\\Program Files\\IIS\\Microsoft Web Deploy V3\\msdeploy.exe" -verb=sync -source:package="%WORKSPACE%\\JenkinsWebApplicationDemo\\bin\\Release\\net6.0\\JenkinsWebApplicationDemo.zip" -dest:auto -setParam:name="IIS Web Application Name",value="JenkinsWebApplicationDemo"  -allowUntrusted=true'
            //bat 'net stop "w3svc"'
            //bat 'net start "w3svc"'
        }
    }
    stage('Deploy Stage AWS') {
        steps {
             echo "Deploy Stage AWS .."
            //Deploy code to s3 bucket
            //bat "aws s3 ls"
            bat "aws s3 sync %WORKSPACE%\\JenkinsWebApplicationDemo\\bin\\Release\\net7.0\\publish s3://dornetapplication"
        }
    }
    
}
}
