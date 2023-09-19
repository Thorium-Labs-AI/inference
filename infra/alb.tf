data aws_acm_certificate api_certificate {
  domain = aws_route53_record.root.name
  tags = ["api-certificate"]
}

resource aws_alb alb {
  name               = var.project_name
  load_balancer_type = "application"
  subnets            = [aws_subnet.subnet_1.id, aws_subnet.subnet_2.id]
  security_groups    = [aws_security_group.alb.id]

  tags = {
    Name = var.project_name
  }
}
resource aws_alb_target_group alb_target_group {
  name        = var.project_name
  port        = 80
  protocol    = "HTTP"
  vpc_id      = aws_vpc.vpc.id
  target_type = "ip"

  health_check {
    enabled  = true
    protocol = "HTTP"
    matcher  = "200-399"
  }
}

resource "aws_alb_listener" "alb_listener" {
  load_balancer_arn = aws_alb.alb.arn
  port              = 443
  protocol          = "HTTPS"
  ssl_policy        = "ELBSecurityPolicy-2016-08"
  certificate_arn   = data.aws_acm_certificate.api_certificate.arn

  default_action {
    type             = "forward"
    target_group_arn = aws_alb_target_group.alb_target_group.arn
  }
}
