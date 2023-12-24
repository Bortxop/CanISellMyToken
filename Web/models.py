# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ContractAbis(models.Model):
    contract_address = models.CharField(unique=True, max_length=42, blank=True, null=True)
    contract_name = models.CharField(max_length=50, blank=True, null=True)
    abi = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contract_abis'


class Contracts(models.Model):
    contract_address = models.CharField(unique=True, max_length=42, blank=True, null=True)
    contract_name = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contracts'


class PoolCreationEvents(models.Model):
    dex = models.CharField(max_length=50, blank=True, null=True)
    token0 = models.CharField(max_length=42, blank=True, null=True)
    token1 = models.CharField(max_length=42, blank=True, null=True)
    pair = models.CharField(max_length=42, blank=True, null=True)
    event = models.CharField(max_length=255, blank=True, null=True)
    logindex = models.IntegerField(blank=True, null=True)
    transactionindex = models.IntegerField(blank=True, null=True)
    transactionhash = models.CharField(max_length=66, blank=True, null=True)
    address = models.CharField(max_length=42, blank=True, null=True)
    blockhash = models.CharField(max_length=66, blank=True, null=True)
    blocknumber = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pool_creation_events'


class TokenReadFunctionsValues(models.Model):
    token_address = models.OneToOneField('Tokens', models.DO_NOTHING, db_column='token_address', blank=True, null=True)
    token_name = models.CharField(max_length=50, blank=True, null=True)
    readfunc1 = models.CharField(max_length=50, blank=True, null=True)
    readfunc2 = models.CharField(max_length=50, blank=True, null=True)
    readfunc3 = models.CharField(max_length=50, blank=True, null=True)
    readfunc4 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'token_read_functions_values'


class Tokens(models.Model):
    address = models.CharField(unique=True, max_length=42, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    symbol = models.CharField(max_length=20, blank=True, null=True)
    decimals = models.IntegerField(blank=True, null=True)
    isbasetoken = models.BooleanField(blank=True, null=True)
    contract_deploy_time = models.DateTimeField(blank=True, null=True)
    contract_deploy_block = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tokens'
