# fmt: off
from yamcs.client import YamcsClient


def print_buckets():
    for bucket in storage_client.list_buckets():
        print(' {} ({} objects, {} bytes)'.format(
            bucket, bucket.object_count, bucket.size))
        listing = bucket.list_objects()
        print('  prefixes:', listing.prefixes)
        for obj in listing.objects:
            print('  object:', obj)


if __name__ == '__main__':
    client = YamcsClient('localhost:8090')
    storage_client = client.get_storage_client()

    print('Buckets:')
    print_buckets()
