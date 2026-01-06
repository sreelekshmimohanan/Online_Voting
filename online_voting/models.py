from django.db import models

class register(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=120)
    password=models.CharField(max_length=120)
    id_proof=models.CharField(max_length=120)
    voter_id=models.CharField(max_length=150, unique=True)
    status=models.CharField(max_length=120, default='pending')  

class election_commission(models.Model):
    staff_id=models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)




class election_tbl(models.Model):
    legislature = models.ForeignKey('legislature', on_delete=models.CASCADE, null=True, blank=True)
    year = models.CharField(max_length=150)
    jurisdiction = models.CharField(max_length=150)
   

class legislature(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

class constituency(models.Model):
    name = models.CharField(max_length=150)
    legislature = models.ForeignKey(legislature, on_delete=models.CASCADE)
    description = models.TextField()


class seat_tbl(models.Model):
    category_id=models.CharField(max_length=150)
    location=models.CharField(max_length=150)
    election_id=models.CharField(max_length=150)
    seat_name=models.CharField(max_length=150)


class candidate_tbl(models.Model):
    constituency = models.ForeignKey('constituency', on_delete=models.CASCADE)
    candidate_name=models.CharField(max_length=150)
    party_name=models.CharField(max_length=150)
    photo=models.CharField(max_length=150)
    legislature = models.ForeignKey('legislature', on_delete=models.CASCADE)
    election = models.ForeignKey('election_tbl', on_delete=models.CASCADE)

class vote_tbl(models.Model):
    election = models.ForeignKey('election_tbl', on_delete=models.CASCADE)
    constituency = models.ForeignKey('constituency', on_delete=models.CASCADE)
    candidate = models.ForeignKey('candidate_tbl', on_delete=models.CASCADE)
    voter = models.ForeignKey('register', on_delete=models.CASCADE)


class result_tbl(models.Model):
    election = models.ForeignKey('election_tbl', on_delete=models.CASCADE)
    constituency = models.ForeignKey('constituency', on_delete=models.CASCADE)
    votes = models.TextField()  # JSON string with candidate_id: vote_count  

class voterlist(models.Model):
    legislature = models.ForeignKey(legislature, on_delete=models.CASCADE)
    constituency = models.ForeignKey(constituency, on_delete=models.CASCADE)
    election = models.ForeignKey(election_tbl, on_delete=models.CASCADE)
    user = models.ForeignKey(register, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='pending')

