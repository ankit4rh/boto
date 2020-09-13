import boto3
import click

session = boto3.Session(profile_name='eva')
ec2 = session.resource('ec2')

def filter_instances(project):
    instances = []

    if project:
        filters = [{'Name':'tag:Project', 'Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()
    return instances

@click.group()
def cli():
    """Eva manages snapshots"""

@cli.group('volumes')
def volumes():
    """Commands for Volumes"""

@cli.group('instances')
def instances():
    """Commands for instances"""

@instances.command('list')
@click.option('--project', default=None,
    help="Only instances for project(tag Project:<name>)")

def list_instances(project):
    "List EC2 instances"

    instances = filter_instances(project)

    for i in instances:
        #converting tags to dictionary
        tags = { t['Key']: t['Value'] for t in i.tags or [] }
        print(', '.join((
        i.id,
        i.instance_type,
        i.placement['AvailabilityZone'],
        i.state['Name'],
        i.public_dns_name,
        tags.get('Project', '<no project>')
        )))
    return

@instances.command('stop')
@click.option('--project', default=None,
    help='Only instances for project')
def stop_instances(project):
    "Stop EC2 Instances"
    instances = []

    instances = filter_instances(project)

    for i in instances:
        print("Stopping {0}...".format(i.id))
        i.stop()
    return

@instances.command('start')
@click.option('--project', default=None,
    help='Only instances for project')
def stop_instances(project):
    "Start EC2 Instances"
    instances = []

    instances = filter_instances(project)

    for i in instances:
        print("Starting {0}...".format(i.id))
        i.start()
    return

@instances.command('reboot')
@click.option('--project', default=None,
    help='Only instances for project')
def stop_instances(project):
    "Reboot EC2 Instances"
    instances = []

    instances = filter_instances(project)

    for i in instances:
        print("Rebooting {0}...".format(i.id))
        i.reboot()
    return


if __name__ == '__main__':
    cli()
