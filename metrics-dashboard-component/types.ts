export interface MetricsReport {
  id: string;
  timestamp: string;
  metrics: {
    [key: string]: number | string;
  };
  changes: string[];
}

export interface MetricsMetadata {
  title: string;
  createdAt: string;
  author: string;
  lastModified: string;
  version: string;
  testResults?: {
    status: 'passed' | 'failed';
    details: string;
  };
  migrationHistory?: {
    version: string;
    date: string;
    changes: string[];
  }[];
}