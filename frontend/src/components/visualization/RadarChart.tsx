import React from 'react';
import { Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, ResponsiveContainer, Legend, Tooltip } from 'recharts';

interface RadarData {
  name: string;
  financial: number;
  career: number;
  lifestyle: number;
  risk: number;
  values: number;
}

export const ScenarioRadarChart: React.FC<{ data: RadarData[] }> = ({ data }) => {
  return (
    <div className="w-full h-96 bg-white rounded-lg shadow-lg p-4">
      <ResponsiveContainer width="100%" height="100%">
        <RadarChart data={data}>
          <PolarGrid />
          <PolarAngleAxis dataKey="name" />
          <PolarRadiusAxis angle={90} domain={[0, 100]} />
          <Radar name="Financial" dataKey="financial" stroke="#2563eb" fill="#2563eb" fillOpacity={0.25} />
          <Radar name="Career" dataKey="career" stroke="#7c3aed" fill="#7c3aed" fillOpacity={0.25} />
          <Radar name="Lifestyle" dataKey="lifestyle" stroke="#10b981" fill="#10b981" fillOpacity={0.25} />
          <Radar name="Risk" dataKey="risk" stroke="#f59e0b" fill="#f59e0b" fillOpacity={0.25} />
          <Radar name="Values" dataKey="values" stroke="#ef4444" fill="#ef4444" fillOpacity={0.25} />
          <Legend />
          <Tooltip />
        </RadarChart>
      </ResponsiveContainer>
    </div>
  );
};
