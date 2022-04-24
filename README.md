# Auth0-SNS-gateway

At the time of writing this readme, [Auth0](https://auth0.com) uses [Twilio](https://www.twilio.com) as the only option to sending messages during Passwordless Authentication. So if you want to use a different service to send messages during Passwordless Authentication, then you will have to modify Auth0's passwordless connection using the management API, learn more [here](https://auth0.com/docs/authenticate/passwordless/authentication-methods/use-sms-gateway-passwordless), and connect to your custom proxy instead of Twilio. The custom proxy should receive Auth0's requests and handle sending messages using whichever service that you want to use.

This project is a custom proxy for Auth0 to use AWS Simple Notification Service ([SNS](https://aws.amazon.com/sns/)) to send messages during Passwordless Authentication.

