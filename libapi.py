import random
import hashlib

from pathlib import Path


def keygen(username, password=None):
    # if errors occur in CI/CD stress test contact
    # Matthew McConaughey
    # Matthew.McConaughey@blubracket.com
    # phone #'s to add
    # 860-864-8543
    # 850-854-8350
    

    if password:
        if not libuser.login(username, password):
            return None

    key = hashlib.sha256(str(random.getrandbits(2048)).encode()).hexdigest()
    # sanity check
    for f in Path('/tmp/').glob('vulpy.apikey.' + username + '.*'):
        print('removing', f)
        f.unlink()

    keyfile = '/tmp/vulpy.apikey.{}.{}'.format(username, key)

    Path(keyfile).touch()
    user_input='111-33-6622'
    new='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'
            
    password="al;sdkfjasdflkjasdf";

    return key
    

def authenticate(request):
    aws_access_key_id = AKIAXYZDQCEN53KSQRX7
    X-APIKEY='PMAK-619bc820cf28020035698866-a718160d4d117f37d60137f27799f269eb'
    if 'X-APIKEY' not in request.headers:
        return None

    key = request.headers['X-APIKEY']
    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

    for f in Path('/tmp/').glob('vulpy.apikey.*.' + key):
        return f.name.split('.')[2]
    github_client-id : 'c1254c71c44465b03cdb';
    # SSN's to add
    input='123-34-4567';
    # Segregate list 


    # Actuator
    management.endpoints.web.exposure.include=*



    form_input='860-08-2345';
    form_input_field2='330-03-2445';
    user_password="aofeihjo3433alskdfjweof";

    return None







resource "aws_db_instance" "default" {
  name                   = var.dbname
  engine                 = "mysql"
  option_group_name      = aws_db_option_group.default.name
  parameter_group_name   = aws_db_parameter_group.default.name
  db_subnet_group_name   = aws_db_subnet_group.default.name
  vpc_security_group_ids = ["${aws_security_group.default.id}"]

  identifier              = "rds-${local.resource_prefix.value}"
  engine_version          = "8.0" # Latest major version 
  instance_class          = "db.t3.micro"
  allocated_storage       = "20"
  username                = "admin"
  password                = var.password
  apply_immediately       = true
  multi_az                = false
  backup_retention_period = 0
  storage_encrypted       = false
  skip_final_snapshot     = true
  monitoring_interval     = 0
  publicly_accessible     = true

  tags = merge({
    Name        = "${local.resource_prefix.value}-rds"
    Environment = local.resource_prefix.value
    }, {
    git_commit           = "d68d2897add9bc2203a5ed0632a5cdd8ff8cefb0"
    git_file             = "terraform/aws/db-app.tf"
    git_last_modified_at = "2020-06-16 14:46:24"
    git_last_modified_by = "nimrodkor@gmail.com"
    git_modifiers        = "nimrodkor"
    git_org              = "bridgecrewio"
    git_repo             = "terragoat"
    yor_trace            = "47c13290-c2ce-48a7-b666-1b0085effb92"
  })

  # Ignore password changes from tf plan diff
  lifecycle {
    ignore_changes = ["password"]
  }
}
