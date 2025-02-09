interface ReportDataCollector {
  // Сбор метрик из различных источников
  collectMetrics(): Promise<MetricsReport[]>;
  
  // Агрегация данных по типам
  aggregateByType(data: MetricsReport[]): AggregatedData;
  
  // Генерация отчета
  generateReport(data: AggregatedData): QuarterlyReport;
}