import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']
    volumes = ec2.describe_volumes()['Volumes']

    active_volume_ids = [vol['VolumeId'] for vol in volumes]

    stale_snapshots = []

    for snap in snapshots:
        if snap.get('VolumeId') not in active_volume_ids:
            stale_snapshots.append(snap['SnapshotId'])

    for snapshot_id in stale_snapshots:
        ec2.delete_snapshot(SnapshotId=snapshot_id)

    return {
        'deleted_snapshots': stale_snapshots,
        'message': 'Stale snapshots removed successfully.'
    }
