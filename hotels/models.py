from django.db import models

class Location(models.Model):
    country = models.CharField(max_length = 30)
    city = models.CharField(max_length=60)
    province = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.city

class Hotel(models.Model):
    """model of hotels"""
    name = models.CharField(max_length = 30)
    star = models.IntegerField()
    address = models.CharField(max_length=50)
    description = models.TextField()
    located  = models.ForeignKey(Location)

    def __unicode__(self):
        return self.name


class Room(models.Model):
    adult = models.IntegerField()  
    children = models.IntegerField()
    belongto = models.ForeignKey(Hotel)
    price = models.FloatField()
    roomNumber = models.IntegerField()

    def __unicode__(self):
        return 'adult: %s, children: %s' % (self.adult, self.children)

class Client(models.Model):
    smoking = models.BooleanField()
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    requirement = models.TextField()
    def __unicode__(self):
        return self.firstname

class Order(models.Model):
    checkin = models.DateField()
    checkout = models.DateField()
    total  = models.FloatField()
    date = models.DateTimeField('Order Date') #create order by date
    client = models.ForeignKey(Client)
    code = models.CharField(max_length=45)
    def __unicode__(self):
        return unicode(self.checkin)

class Booked(models.Model):
    room = models.ForeignKey(Room)
    order = models.ForeignKey(Order)
    def __unicode__(self):
        return unicode(self.room) + ' ' + unicode(self.order)

