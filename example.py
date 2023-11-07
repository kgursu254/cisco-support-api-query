"""Example usage of Cisco Support API utilities
"""

import csv
from dotenv import dotenv_values
from util.api_login import ApiLogin
from util.api_eox import ApiEox


def main():

    api = ApiLogin('h9mrtrht6kvckq7cuvh2qqzj', '9vhW3wgHMM5mC56xSexAneut')
    eox = ApiEox(api.auth_token)
    pids = ['LIC-VVCS-C-M-PAK', 'L-ISE-BSE-P5', 'M-ASR1002X-8GB', ]
    eox.query_by_pid(pids)

    FNAME = 'eox_report.csv'
    with open(FNAME, mode='w') as fhand:
        writer = csv.writer(fhand, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['EOLProductID',
                         'ProductIDDescription',
                         'LastDateOfSupport',
                         'EndOfSWMaintenanceReleases',
                         'EOXExternalAnnouncementDate',
                         'EndOfSaleDate',
                         'EndOfSecurityVulSupportDate',
                         'EndOfRoutineFailureAnalysisDate',
                         'EndOfServiceContractRenewal',
                         'EndOfSvcAttachDate',
                         'LinkToProductBulletinURL', ])
        for record in eox.records:
            writer.writerow([record['EOLProductID'],
                             record['ProductIDDescription'],
                             record['LastDateOfSupport']['value'],
                             record['EndOfSWMaintenanceReleases']['value'],
                             record['EOXExternalAnnouncementDate']['value'],
                             record['EndOfSaleDate']['value'],
                             #record['EndOfSecurityVulSupportDate']['value'],
                             record['EndOfRoutineFailureAnalysisDate']['value'],
                             record['EndOfServiceContractRenewal']['value'],
                             record['EndOfSvcAttachDate']['value'],
                             record['LinkToProductBulletinURL'], ])

    print(f'EOX records written to file {FNAME}')


if __name__ == "__main__":
    main()
