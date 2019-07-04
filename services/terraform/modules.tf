# This file sources the available Terraform modules: one for the Gateway and one for Analytics.

# If you do not wish to deploy the gateway, comment out the gateway section below!

module "gateway" {
  source           = "./module-gateway"
  gcloud_project   = "${var.gcloud_project}"
  gcloud_region    = "${var.gcloud_region}"
  gcloud_zone      = "${var.gcloud_zone}"
  k8s_cluster_name = "${var.k8s_cluster_name}"
}

output "gateway_host" {
  value = module.gateway.gateway_host
}

output "gateway_dns" {
  value = module.gateway.gateway_dns
}

output "party_host" {
  value = module.gateway.party_host
}

output "party_dns" {
  value = module.gateway.party_dns
}

output "playfab_auth_host" {
  value = module.gateway.playfab_auth_host
}

output "playfab_auth_dns" {
  value = module.gateway.playfab_auth_dns
}

# If you do not wish to deploy analytics, comment out the analytics section below!

module "analytics" {
  source                           = "./module-analytics"
  gcloud_analytics_bucket_location = "EU"
  gcloud_region                    = "${var.gcloud_region}"
  gcloud_project                   = "${var.gcloud_project}"
}

output "analytics_host" {
  value = module.analytics.analytics_host
}

output "analytics_dns" {
  value = module.analytics.analytics_dns
}
