from includes.config import *
from utils.tools import *
import requests
import logging

msg = """
🚨 @harmonyprotocol $ONE Governance Proposal🚨

HIP-15: Validator Governance Participation Indicator

Proposal to show validator participation in governance votes on staking dashboard

Increase validator participation in governance

✍️Talk: https://talk.harmony.one/t/hip-15-validator-governance-participation-indicator/1836

#VDaoDotOne

"""
post_url = f"https://graph.facebook.com/{PAGE_ID}/feed"
payload = {"message": msg, "access_token": FB_ACCESS_TOKEN}
r = requests.post(post_url, data=payload)
print(r.json())
