from django.db import models

class register(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=120)
    password=models.CharField(max_length=120)
    id_proof=models.CharField(max_length=120)
    status=models.CharField(max_length=120, default='pending')  

class election_commission(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)




class election_tbl(models.Model):
    category=models.CharField(max_length=150)
    year=models.CharField(max_length=150)
   

class seat_tbl(models.Model):
    category_id=models.CharField(max_length=150)
    location=models.CharField(max_length=150)
    election_id=models.CharField(max_length=150)
    seat_name=models.CharField(max_length=150)


class candidate_tbl(models.Model):
    seat_id=models.CharField(max_length=150)
    candidate_name=models.CharField(max_length=150)
    party_name=models.CharField(max_length=150)
    photo=models.CharField(max_length=150)
    location=models.CharField(max_length=150)
    seat=models.CharField(max_length=150)

class vote_tbl(models.Model):
    election_id=models.CharField(max_length=150)
    seat_id=models.CharField(max_length=150)
    candidate_id=models.CharField(max_length=150)
    voter_id=models.CharField(max_length=150)


class result_tbl(models.Model):
    election_id=models.CharField(max_length=150)
    seat_id=models.CharField(max_length=150)
    candidate_id=models.CharField(max_length=150)
    votes=models.CharField(max_length=150)



class election_commission(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)    
    

