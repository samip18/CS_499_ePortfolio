-- Schema creation
CREATE SCHEMA  `buppa-gump-snhu.demo` ;


-- external table creation to read from parquet
DROP TABLE IF EXISTS `buppa-gump-snhu.reports_buppa_gump.state_customer_revenue_report`;

CREATE EXTERNAL TABLE `buppa-gump-snhu.reports_buppa_gump.state_customer_revenue_report` 
(
  state STRING,
  visit_total INT64,
  total_earning FLOAT64
) 
OPTIONS (
  uris=['gs://report_store_buppa_gump/state_customer_revenue_report.parquet/*'],
  format=parquet
);
