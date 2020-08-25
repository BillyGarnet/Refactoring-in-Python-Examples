# bad method names

def gt_cd(st_rgn):
    if st_rgn == 1:
        return 'Somewhere'
    else:
        return 'Elsewhere'


def process(site):
    site.region = gt_cd(1) if site > 5 else gt_cd(2)


def send_site_to_process_system_for_assignment_of_region_codes(site):
    # do work on site
    process(site)


def process_item(self, region, location):
    if region in location:
        send_site_to_process_system_for_assignment_of_region_codes(region)
    else:
        send_site_to_process_system_for_assignment_of_region_codes(location)
