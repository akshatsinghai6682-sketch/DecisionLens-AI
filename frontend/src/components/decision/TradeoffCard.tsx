import React from 'react';
import { AlertCircle } from 'lucide-react';

interface TradeoffCardProps {
  description: string;
  category: string;
  impact: 'high' | 'medium' | 'low';
  hiddenNature: string;
  onAcknowledge: () => void;
  acknowledged: boolean;
}

export const TradeoffCard: React.FC<TradeoffCardProps> = ({
  description,
  category,
  impact,
  hiddenNature,
  onAcknowledge,
  acknowledged,
}) => {
  const impactColor = impact === 'high' ? 'text-red-600' : impact === 'medium' ? 'text-yellow-600' : 'text-green-600';

  return (
    <div className={`border-l-4 rounded-lg p-4 mb-4 ${
      acknowledged ? 'border-green-500 bg-green-50' : 'border-amber-500 bg-amber-50'
    }`}>
      <div className="flex items-start gap-3">
        <AlertCircle className="text-amber-600 flex-shrink-0 mt-1" size={20} />
        <div className="flex-1">
          <h3 className="font-semibold text-gray-900">{description}</h3>
          <p className="text-sm text-gray-700 mt-1">Category: <span className="font-medium">{category}</span></p>
          <p className={`text-sm font-semibold mt-1 ${impactColor}`}>Impact: {impact.toUpperCase()}</p>
          <p className="text-sm text-gray-600 mt-2 italic">{hiddenNature}</p>
          <button
            onClick={onAcknowledge}
            className={`mt-3 px-3 py-1 rounded text-sm font-medium transition ${
              acknowledged
                ? 'bg-green-200 text-green-800'
                : 'bg-white text-gray-700 border border-gray-300 hover:bg-gray-50'
            }`}
          >
            {acknowledged ? '✓ Acknowledged' : 'Acknowledge'}
          </button>
        </div>
      </div>
    </div>
  );
};
