import React from 'react';
import { MetricsReport, MetricsMetadata } from './types';

interface MetricsDashboardProps {
  data: MetricsReport[];
  metadata: MetricsMetadata;
  onUpdate?: (report: MetricsReport) => void;
}

export const MetricsDashboard: React.FC<MetricsDashboardProps> = ({
  data,
  metadata,
  onUpdate
}) => {
  return (
    <div className="metrics-dashboard">
      <header className="metrics-header">
        <h1>{metadata.title}</h1>
        <div className="metadata">
          <span>Created: {metadata.createdAt}</span>
          <span>Author: {metadata.author}</span>
        </div>
      </header>
      <main className="metrics-content">
        {/* Metrics visualization components will go here */}
      </main>
    </div>
  );
};