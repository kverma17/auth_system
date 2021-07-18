data = {'admin':{'role':['ADMIN_ACCESS']},'user1':{'role':['HR_READ_ACCESS']}}

roles = {
    'ADMIN_ACCESS': {
        'ACTION_TYPE': ['Read', 'Write', 'Delete'],
        'RESOURCE'   : ['HR Material', 'Cloud Material', 'ERP Material'],
    },
    'HR_READ_ACCESS' : {
        'ACTION_TYPE': ['Read'],
        'RESOURCE'   : ['HR Material'],
    },
    'HR_WRITE_ACCESS': {
        'ACTION_TYPE': ['Read', 'Write'],
        'RESOURCE'   : ['HR Material', 'ERP Material'],
    },
    'DEV_WRITE_ACCESS': {
        'ACTION_TYPE': ['Read', 'Write'],
        'RESOURCE'   : ['Cloud Material'],
    },
}