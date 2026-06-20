import React from 'react';

interface ConfidenceMeterProps {
  confidence: number;
  label?: string;
}

export const ConfidenceMeter: React.FC<ConfidenceMeterProps> = ({ confidence, label = 'Confidence Level' }) => {
  const percentage = Math.round(confidence * 100);
  const bgColor =
    percentage >= 75 ? 'bg-green-500' : percentage >= 50 ? 'bg-yellow-500' : 'bg-red-500';

  return (
    <div className="bg-white rounded-lg shadow p-4">
      <p className="text-sm font-semibold text-gray-700 mb-2">{label}</p>
      <div className="w-full bg-gray-200 rounded-full h-4 overflow-hidden">
        <div className={`${bgColor} h-full transition-all duration-300`} style={{ width: `${percentage}%` }}></div>
      </div>
      <p className="text-right text-sm font-bold text-gray-700 mt-2">{percentage}%</p>
    </div>
  );
};
