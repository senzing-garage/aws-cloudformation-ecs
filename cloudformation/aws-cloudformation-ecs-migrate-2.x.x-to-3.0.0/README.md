# aws-cloudformation-ecs-migrate-2.x.x-to-3.0.0

For use in migrating the Senzing Aurora database from Senzing 2.x.x to 3.0.0.
This is meant to be a temporary stack used to run a couple of migration commands
against a 2.x.x database to prepare it for a 3.0.0 installation.

### Launch AWS Cloudformation

1. :thinking: **Warning:** This Cloudformation deployment will accrue AWS costs.
   With appropriate permissions, the
   [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
   can help evaluate costs.
1. Visit [AWS Cloudformation console](https://console.aws.amazon.com/cloudformation/home)
1. In upper-right, click "Create stack" > "With new resources (standard)"
1. In **Create stack** page
    1. Check ":radio_button: Upload a temporary file"
    1. Click "Choose file" button
    1. Select local copy of [cloudformation.yaml](cloudformation.yaml)
    1. In lower-right, click on "Next" button.
1. In **Specify stack details**
    1. In **Stack name**
        1. Make a stack starting with a unique name.
           Example:
            1. `sz-migrate`
    1. In **Parameters**
        1. In **Senzing installation**
            1. Accept the End User License Agreement
            1. Select the version of Senzing you want to install from the drop down.
               Example: `3.0.0`
            1. Input your Base64 license, as needed.
        1. In **Identify existing resources**
            1. Enter the stack name of the previously deployed 2.x.x
               [aws-cloudformation-database-cluster](https://github.com/senzing-garage/aws-cloudformation-database-cluster)
               Cloudformation stack
               Example:  `senzing-db`
        1. In **Security**
            1. Enter your email address.  Example: `me@example.com`
            1. Prove an appropriate CIDR block.
        1. In **Security responsibility**
            1. Understand the nature of the security in the deployment.
            1. Once understood, enter "I AGREE".
    1. In lower-right, click "Next" button.
1. In **Configure stack options**
    1. In lower-right, click "Next" button.
1. In **Review {stack-name}**
    1. Near the bottom, in **Capabilities**
        1. Check ":ballot_box_with_check: I acknowledge that AWS CloudFormation might create IAM resources."
    1. In lower-right, click "Create stack" button.

## Migration

1. Visit [AWS Cloudformation console](https://console.aws.amazon.com/cloudformation/home)
1. Choose cloudformation stack that was deployed for testing
1. Choose "Outputs" tab
    1. Open value for **0penFirst** in a new browser tab
        1. Page will show warning because of the self-signed certificate used for HTTPS by the Application Load Balancer.
           Figure out how to proceed past the warning.
        1. You will be prompted for email and password.
           From the "Outputs" tab, use **UserName** and **UserInitPassword** values.
        1. Supply a new password.
    1. Open value for **UrlXterm** in a new browser tab
        1. In XTerm window, to automatically upgrade your database, enter:
            1. `/opt/senzing/g2/bin/g2dbupgrade -c /etc/opt/senzing/G2Module.ini -a`
                (Note: if you are running with a single database, you may see a database error, this can safely be ignored.)
            1. `/opt/senzing/g2/bin/g2configupgrade -c /etc/opt/senzing/G2Module.ini -s /opt/senzing/g2/python -a`
        1. IF YOU DON'T WANT TO AUTOMATICALLY UPGRADE
            1. `/opt/senzing/g2/bin/g2dbupgrade -c /etc/opt/senzing/G2Module.ini -o /var/opt/senzing`
            1. `/opt/senzing/g2/bin/g2configupgrade -c /etc/opt/senzing/G2Module.ini --o /var/opt/senzing`
            1. Review the generated files and maunally update.
1. Your migration is complete.
1. You many now delete this migration stack and install the Basic or Choices stack.
