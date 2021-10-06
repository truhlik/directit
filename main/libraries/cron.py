# coding: utf-8
# from django.conf import settings
# from django_cron import CronJobBase, Schedule
# from main.libraries.decorators import sentry_exceptions

# class StaticFileDownloader(CronJobBase):
#     """
#     Cron job updating files defined in static_files_dict from url.
#     """
#     RUN_AT_TIMES = ['02:00']
#     RETRY_AFTER_FAILURE_MINS = 5
#
#     schedule = Schedule(run_at_times=RUN_AT_TIMES, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
#     code = 'libraries.static_file_downloader_cron_job'  # a unique code
#
#     @sentry_exceptions
#     def do(self):
#         import requests
#         import os
#         # global dump
#         REMOTE_STATIC_PATH = settings.STATIC_ROOT + '/remote/'
#
#         # put here all distant static files which should be periodically downloaded
#         static_files_dict = [
#              {'url': 'https://www.google-analytics.com/analytics.js', 'path': REMOTE_STATIC_PATH + '/analytics.js'},
#         ]
#
#         if not os.path.isdir(REMOTE_STATIC_PATH):
#             os.mkdir(REMOTE_STATIC_PATH, 0o775)
#
#         for file_item in static_files_dict:
#             file = requests.get(file_item['url'], stream=True)
#
#             with open(os.path.abspath(file_item['path']), 'wb') as location:
#                 for chunk in file.iter_content(1024):
#                     location.write(chunk)
