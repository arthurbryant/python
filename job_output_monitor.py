import sys
import logging
import boto3
import datetime
from urllib import urlencode
import urllib2 as urlrequest
import json
import os


logger = logging.getLogger()
logger.setLevel(logging.INFO)
SLACK_POST_URL = os.environ['SLACK_URL']

def handler(event, context):
    check_job_output('staging')
    check_job_output('production')

def check_job_output(env):
    s3 = boto3.client('s3')
    tdatetime = datetime.datetime.now() - datetime.timedelta(days=1)
    target_date = tdatetime.strftime('%Y%m%d')
    logger.info(target_date)
    bucket_name = 'fout-fox-' + env
    empty_logs = getEmptyLog(bucket_name, s3, target_date)
    if len(empty_logs) != 0:
        slack_message = get_slack_message(bucket_name, empty_logs, target_date, env)
        post(slack_message)

def get_slack_message(bucket_name,empty_logs, target_date, env):
   mention = 
       if env == 'production'
           mention = "<!subteam^S286FGKSA|ase_dev_team>" : ''
           else
               mention = ''
                 
    mention = env == 'production' ? "<!subteam^S286FGKSA|ase_dev_team>" : ''
    slack_message = {
        'username': "AWS EMR JobOutput",
        'attachments': [
            {
                'color': "warning",
                "title": "EMR Job Output Result",
                'text': "<!subteam^S286FGKSA|ase_dev_team> %s S3 log is empty on %s \n Env: %s" % (",".join(empty_logs),target_date,bucket_name)
            }
        ]
    }
    logger.info(slack_message)
    return slack_message

def getEmptyLog(bucket_name, s3, target_date):
    prefixes = ['audienceLog', 'hourlySummary', 'dailyAvgtimeSummary', 'estimatedSeikatsukenSummary',
                'estimatedSeikatsukenAvgtimeSummary', 'livingAreaEstimateSummaryBase', 'livingAreaEstimateResult',
                'pointToPointSummary', 'dailyUserReport', 'demograUpdateAudiences']
    empty_logs = []
    for prefix in prefixes:
        response = s3.list_objects(Bucket=bucket_name, Prefix='job-output/' + prefix + '/' + target_date + '/')
        if not is_succeeded(response):
            empty_logs.append(prefix)
    logger.info(empty_logs)
    return empty_logs
    
def is_succeeded(response):
    if 'Contents' in response:
        for content in response['Contents']:
            file_name = os.path.basename(content['Key'])
            if '_SUCCESS' == file_name:
                return True
        return False

def post(msg):
    msg_json = json.dumps(msg)
    data = urlencode({"payload": msg_json})
    logger.info(data)
    req = urlrequest.Request(SLACK_POST_URL)
    response = urlrequest.build_opener(urlrequest.HTTPHandler()).open(req, data.encode('utf-8')).read()
    return response.decode('utf-8')
