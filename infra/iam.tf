# ECS Execution Role
resource aws_iam_role ecs_execution_role {
  name               = "${var.project_name}-ecs-task-execution-role"
  assume_role_policy = data.aws_iam_policy_document.assume.json
}

data aws_iam_policy_document assume {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["ecs-tasks.amazonaws.com"]
    }
  }
}

data aws_iam_policy_document ecs_execution_role_policy {
  statement {
    effect    = "Allow"
    actions   = ["ecr:GetDownloadUrlForLayer", "ecr:BatchGetImage", "ecr:GetAuthorizationToken", "logs:CreateLogStream"]
    resources = ["*"]
  }
}

resource aws_iam_policy ecs_execution_policy {
  name   = "${var.project_name}-ecs-execution-policy"
  policy = data.aws_iam_policy_document.ecs_execution_role_policy.json
}

resource aws_iam_role_policy_attachment ecs_execution_role_policy_attachment {
  role       = aws_iam_role.ecs_execution_role.name
  policy_arn = aws_iam_policy.ecs_execution_policy.arn
}


# ECS Task Policy

resource aws_iam_role ecs_task_role {
  name               = "${var.project_name}-ecs-task-role"
  assume_role_policy = data.aws_iam_policy_document.assume.json
}

resource aws_iam_role_policy_attachment ecs_task_execution_role_policy_attachment {
  role       = aws_iam_role.ecs_task_role.name
  policy_arn = aws_iam_policy.task_role_policy.arn
}

resource aws_iam_policy ecs_task_execution_role_policy {
  name   = "${var.project_name}-ecs-task-role-policy"
  policy = data.aws_iam_policy_document.ecs_task_role_policy.json
}

data aws_iam_policy_document ecs_task_role_policy {
  statement {
    effect  = "Allow"
    actions = [
      "dynamodb:PutItem",
      "dynamodb:GetItem",
      "dynamodb:BatchGetItem",
      "dynamodb:DeleteItem",
      "dynamodb:UpdateItem",
      "dynamodb:DescribeTable",
      "dynamodb:Query"
    ]

    resources = ["*"]
  }
}

resource "aws_iam_policy" "task_role_policy" {
  name        = "${var.project_name}-ecs-task-policy"
  description = "A test policy"
  policy      = data.aws_iam_policy_document.ecs_task_role_policy.json
}

resource aws_iam_role_policy_attachment ecs_task_execution_attachment {
  role       = aws_iam_role.ecs_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}