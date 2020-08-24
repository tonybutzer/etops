import subprocess
import argparse
import boto3

def get_parser():
    parser = argparse.ArgumentParser(description='Sync the directory to a new location and verify - then delete')
    parser.add_argument('-s', '--src', help='specify the src dir to move', default='none', type=str)
    parser.add_argument('-d', '--dst', help='specify the dst directory final resting place', default='none', type=str)
    return parser


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['src']:
        print("src", args['src'])
        src = args['src']
    if args['dst']:
        print("dst", args['dst'])
        dst = args['dst']

    bucket = src.split('/')[0]
    prefix = '/'.join(src.split('/')[1:])
    s3_list = return_s3_list(bucket, prefix)

    byte_sum = 0
    for (obj,length) in s3_list:
        print(obj, length)
        byte_sum = byte_sum + length

    print("\nTotal Objects = ", len(s3_list))
    print("\tTotal Bytes = ", byte_sum)


    ### sync the src to dst
    s3sync(src,dst)


    ###

    bucket = dst.split('/')[0]
    prefix = '/'.join(dst.split('/')[1:])
    dst_s3_list = return_s3_list(bucket, prefix)

    dst_byte_sum = 0
    for (obj,length) in dst_s3_list:
        print(obj, length)
        byte_sum = byte_sum + length

    print("\nTotal Objects = ", len(s3_list))
    print("\tTotal Bytes = ", dst_byte_sum)

    if dst_byte_sum != byte_sum:
        print("BUMMER")


#### S3 Stuff

def return_s3_list(working_bucket, prefix):
        aws_list = []
        s3 = boto3.resource('s3')
        bucket_name = working_bucket
        bucket = s3.Bucket(bucket_name)
        for obj in bucket.objects.filter(Prefix=prefix):
            aws_list.append((obj.key, obj.size))
        return aws_list


def subprocess_cmd(command):
    print ("+++"*20)
    print ("CMD is -- %s" % command)
    print ("+++"*20)
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    stupidBytesObject = proc_stdout
    outStr = (stupidBytesObject.decode("utf-8"))
    print(outStr)
    return(outStr)


def s3sync(src,dst):
        src = 's3://' + src
        dst = 's3://' + dst
        print ("hello from s3sync copying dir " + src)
        print ("hello from s3sync copying to dir " + dst)
        pushcmd = "aws s3 sync %s %s" % (src, dst)
        print (pushcmd)
        subprocess_cmd(pushcmd)

if __name__ == '__main__':
    command_line_runner()

