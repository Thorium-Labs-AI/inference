resource "aws_route53_zone" "main" {
  name = "asterisk.chat"
}

resource "aws_route53_record" "www" {
  zone_id = aws_route53_zone.main.zone_id
  name    = "www.api.asterisk.chat"
  type    = "A"

  alias {
    name                   = aws_alb.alb.dns_name
    zone_id                = aws_alb.alb.zone_id
    evaluate_target_health = true
  }
}

resource "aws_route53_record" "root" {
  zone_id = aws_route53_zone.main.zone_id
  name    = "asterisk.chat"
  type    = "A"

  alias {
    name                   = aws_alb.alb.dns_name
    zone_id                = aws_alb.alb.zone_id
    evaluate_target_health = true
  }
}


resource aws_acm_certificate acm_certificate {
  certificate_authority_arn = "arn:aws:acm:us-east-1:883869506849:certificate/778ef356-1812-49e8-9bf1-9943a664e470"
}