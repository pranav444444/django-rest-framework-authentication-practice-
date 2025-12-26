from rest_framework.throttling import UserRateThrottle

class JackRateThrottle(UserRateThrottle): #inherit userrate throttle in jackratetrottle scope throttle class
  scope='jack'