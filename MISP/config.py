
'''This Config python file have tenant id, cliend id and MISP key for accessing MISP portal Events
and also have misp domain name, misp event filter'''

graph_auth = {
    'tenant': 'e9dcd40a-373d-46f5-9921-22ca71ba9aec',
    'client_id': 'f7c0550b-2c9b-4a01-a0e0-ffad88844aaa',
    'client_secret': 'ju6jvrx?oLNI5PQ[6BG_6@qerDvT/a50',
}
targetProduct = "Azure Sentinel"
misp_event_filters = [
    {
        "eventid": '1246'
    }
]
action = "allow"
passiveOnly = False
days_to_expire = 20
misp_key = 'uEyCUfITmAlzK22vdiQkxiEjoH294x4rteug4iya'
misp_domain = 'https://192.168.0.22/'
misp_verifycert = False

